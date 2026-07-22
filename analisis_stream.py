import pandas as pd 
import matplotlib.pyplot as plt

datos=pd.read_excel("usuarios_streaming.xlsx")

datos.info()
print(datos.head())

#Filtrado por condiciones de cancelacion 
cancelados=datos[datos["Estatus"]=="Cancelado"]
print(cancelados.head())

#Calculamos el promedio de los cancelados
promedio_cancelados = cancelados["Soporte_Tecnico"].mean()
print(f"El promedio de soporte técnico para los usuarios cancelados es: {promedio_cancelados}")

#Filtrado por condiciones de activos 
Activos=datos[datos["Estatus"]=="Activo"]
print(Activos.head())

promedio_activos = Activos["Soporte_Tecnico"].mean()
print(f"El promedio de soporte técnico para los usuarios activos es: {promedio_activos}")

promedio_soporte = pd.Series ([promedio_cancelados, promedio_activos], index=["Cancelados", "Activos"])

promedio_soporte.plot(kind="bar", color = ["red", "green"])
plt.title("Promedio de Soporte Técnico por Estatus")
plt.ylabel("Promedio de Soporte Técnico")
plt.xlabel("Estatus")
plt.ylim(0, 5)
plt.show()








