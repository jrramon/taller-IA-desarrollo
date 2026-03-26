"""
Genera datos de producción realistas para el taller.
Los datos tienen patrones intencionados para que el análisis sea interesante.
"""

import csv
import random
from datetime import datetime, timedelta

random.seed(42)

LINEAS = ["L1", "L2"]
TURNOS = [
    ("mañana", "06:00", "14:00"),
    ("tarde", "14:00", "22:00"),
    ("noche", "22:00", "06:00"),
]

PRODUCTOS_L1 = ["PIEZA-A", "PIEZA-A", "PIEZA-A", "PIEZA-C"]  # L1 hace sobre todo PIEZA-A
PRODUCTOS_L2 = ["PIEZA-B", "PIEZA-B", "PIEZA-B", "PIEZA-A"]  # L2 hace sobre todo PIEZA-B

CAUSAS_PARADA = [
    ("averia_mecanica", 0.35),
    ("cambio_molde", 0.20),
    ("ajuste_parametros", 0.18),
    ("falta_material", 0.12),
    ("averia_electrica", 0.08),
    ("limpieza", 0.05),
    ("otro", 0.02),
]

CAPACIDAD = {"L1": 1250, "L2": 850}

# Parámetros base por línea
TEMP_BASE = {"L1": 185.0, "L2": 210.0}
PRESION_BASE = {"L1": 3.1, "L2": 4.2}
VELOCIDAD = {"L1": 45, "L2": 30}


def elegir_causa():
    r = random.random()
    acum = 0
    for causa, prob in CAUSAS_PARADA:
        acum += prob
        if r <= acum:
            return causa
    return "otro"


def generar_registro(linea, turno, turno_inicio, turno_fin, fecha):
    es_noche = turno == "noche"
    es_lunes = fecha.weekday() == 0
    es_viernes = fecha.weekday() == 4

    productos = PRODUCTOS_L1 if linea == "L1" else PRODUCTOS_L2
    producto = random.choice(productos)
    es_pieza_c = producto == "PIEZA-C"

    capacidad = CAPACIDAD[linea]
    if es_pieza_c:
        capacidad = int(capacidad * 0.78)
        velocidad = 40
    else:
        velocidad = VELOCIDAD[linea]

    # --- Temperatura ---
    temp_base = TEMP_BASE[linea]
    temp = temp_base + random.gauss(0, 0.8)
    if es_noche:
        temp += random.gauss(5, 2.5)  # noche: temperatura sube
    if es_pieza_c:
        temp += random.gauss(1.5, 0.5)

    # --- Presión ---
    presion_base = PRESION_BASE[linea]
    presion = presion_base + random.gauss(0, 0.1)
    if es_noche:
        presion -= random.gauss(0.2, 0.1)  # noche: presión baja
    presion = round(max(presion, 2.0), 1)

    # --- Paradas ---
    if es_noche:
        prob_parada = 0.75
    elif turno == "tarde":
        prob_parada = 0.45
    else:
        prob_parada = 0.20

    if es_lunes:
        prob_parada += 0.10  # lunes: más problemas al arrancar

    hay_parada = random.random() < prob_parada
    if hay_parada:
        causa = elegir_causa()
        # Noche L2 tiene más averías eléctricas
        if es_noche and linea == "L2" and random.random() < 0.35:
            causa = "averia_electrica"
        # Avería mecánica dura más
        if causa == "averia_mecanica":
            tiempo_parada = int(random.gauss(40, 15))
        elif causa in ("cambio_molde", "cambio_producto"):
            tiempo_parada = int(random.gauss(18, 5))
        elif causa == "averia_electrica":
            tiempo_parada = int(random.gauss(50, 20))
        elif causa == "falta_material":
            tiempo_parada = int(random.gauss(35, 12))
        else:
            tiempo_parada = int(random.gauss(10, 5))
        tiempo_parada = max(3, min(tiempo_parada, 120))
    else:
        causa = ""
        tiempo_parada = 0

    # --- Producción ---
    disponibilidad = (480 - tiempo_parada) / 480
    base_rendimiento = 0.92 if turno == "mañana" else (0.88 if turno == "tarde" else 0.78)
    if es_pieza_c:
        base_rendimiento -= 0.05
    if es_viernes:
        base_rendimiento -= 0.03
    rendimiento = base_rendimiento + random.gauss(0, 0.03)
    rendimiento = max(0.5, min(rendimiento, 1.0))

    unidades = int(capacidad * disponibilidad * rendimiento)
    unidades = max(100, unidades)

    # --- Defectos ---
    tasa_defectos_base = 0.012  # 1.2%
    if es_noche:
        tasa_defectos_base += 0.025
    if es_pieza_c:
        tasa_defectos_base += 0.015
    # Temperatura alta → más defectos
    exceso_temp = max(0, temp - (temp_base + 3))
    tasa_defectos_base += exceso_temp * 0.004
    # Presión baja → más defectos
    deficit_presion = max(0, presion_base - 0.3 - presion)
    tasa_defectos_base += deficit_presion * 0.01

    tasa_defectos = tasa_defectos_base + random.gauss(0, 0.005)
    tasa_defectos = max(0.002, min(tasa_defectos, 0.12))

    defectuosas = int(unidades * tasa_defectos)
    defectuosas = max(0, defectuosas)

    return {
        "linea": linea,
        "turno": turno,
        "fecha": fecha.strftime("%Y-%m-%d"),
        "hora_inicio": turno_inicio,
        "hora_fin": turno_fin,
        "producto": producto,
        "unidades_producidas": unidades,
        "unidades_defectuosas": defectuosas,
        "tiempo_parada_min": tiempo_parada,
        "causa_parada": causa,
        "temperatura_horno": round(temp, 1),
        "presion_bar": presion,
        "velocidad_linea": velocidad,
    }


def main():
    fecha_inicio = datetime(2026, 2, 23)  # lunes
    dias = 56  # 8 semanas

    registros = []
    for d in range(dias):
        fecha = fecha_inicio + timedelta(days=d)
        if fecha.weekday() >= 5:  # saltar fines de semana
            continue
        for linea in LINEAS:
            for turno, inicio, fin in TURNOS:
                registros.append(generar_registro(linea, turno, inicio, fin, fecha))

    campos = [
        "linea", "turno", "fecha", "hora_inicio", "hora_fin", "producto",
        "unidades_producidas", "unidades_defectuosas", "tiempo_parada_min",
        "causa_parada", "temperatura_horno", "presion_bar", "velocidad_linea",
    ]

    with open("datos_produccion.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(registros)

    print(f"Generados {len(registros)} registros en datos_produccion.csv")

    # Resumen rápido
    turnos_noche = [r for r in registros if r["turno"] == "noche"]
    turnos_dia = [r for r in registros if r["turno"] != "noche"]
    def_noche = sum(r["unidades_defectuosas"] for r in turnos_noche) / sum(r["unidades_producidas"] for r in turnos_noche)
    def_dia = sum(r["unidades_defectuosas"] for r in turnos_dia) / sum(r["unidades_producidas"] for r in turnos_dia)
    print(f"Tasa defectos noche: {def_noche:.1%} vs día: {def_dia:.1%}")
    print(f"Paradas noche: {sum(1 for r in turnos_noche if r['tiempo_parada_min'] > 0)}/{len(turnos_noche)}")
    print(f"Paradas día: {sum(1 for r in turnos_dia if r['tiempo_parada_min'] > 0)}/{len(turnos_dia)}")


if __name__ == "__main__":
    main()
