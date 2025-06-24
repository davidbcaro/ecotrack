
from core.models import Pais, PoliticaClimatica, AcuerdoInternacional, PaisAcuerdo, AlertaEmision, Emision, SectorEconomico

def run():
    # Sectores
    transporte = SectorEconomico.objects.create(nombre_sector="Transporte", descripcion="Emisiones del sector transporte")
    energia = SectorEconomico.objects.create(nombre_sector="Energía", descripcion="Producción y consumo de energía")

    # Países
    colombia = Pais.objects.create(nombre="Colombia", region="América del Sur", poblacion=51800000, pib=314.5)
    alemania = Pais.objects.create(nombre="Alemania", region="Europa", poblacion=83000000, pib=4000.0)

    # Acuerdos
    paris = AcuerdoInternacional.objects.create(nombre="Acuerdo de París", fecha_firma="2015-12-12", descripcion="Reducir emisiones globales")
    kioto = AcuerdoInternacional.objects.create(nombre="Protocolo de Kioto", fecha_firma="1997-12-11", descripcion="Tratado sobre cambio climático")

    # Relación país-acuerdo
    PaisAcuerdo.objects.create(pais=colombia, acuerdo=paris, fecha_adhesion="2016-09-21")
    PaisAcuerdo.objects.create(pais=alemania, acuerdo=paris, fecha_adhesion="2016-10-01")
    PaisAcuerdo.objects.create(pais=alemania, acuerdo=kioto, fecha_adhesion="1999-03-01")

    # Políticas climáticas
    PoliticaClimatica.objects.create(
        pais=colombia,
        titulo="Plan Nacional de Cambio Climático",
        descripcion_politica="Reducción del 51% de emisiones para 2030",
        fecha_publicacion="2020-08-01"
    )

    # Emisiones
    Emision.objects.create(pais=colombia, sector=transporte, fecha="2024-01-01", cantidad_co2e=125000.750)
    Emision.objects.create(pais=alemania, sector=energia, fecha="2024-01-01", cantidad_co2e=300000.500)

    # Alertas de emisión
    AlertaEmision.objects.create(
        pais=colombia,
        umbral=100000.000,
        valor_emision=125000.750,
        fecha_alerta="2024-01-05",
        estado="Activa"
    )

    print("✅ Datos de ejemplo cargados correctamente.")
