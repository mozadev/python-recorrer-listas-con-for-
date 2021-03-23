
def run():# funcion principal

	#--------------almacenando en una lista--------------------------

	lista_planetas=["Mercurio", "Venus", "Tierra", "Marte", "Jupiter", "Saturno", "Urano", "Neptuno", "Pluton", "Luna"]
	velocidad_escape=[4.2, 10.3, 11.2, 5.0, 61.0, 36.0, 22.0, 24.0, 5.3, 2.4]
	planeta=input("Digite un planeta (Mercurio,Venus,Tierra,Marte,Jupiter,Saturno,Urano,Neptuno,Pluton,Luna): ")
	planeta=planeta.capitalize()

	for i in range(len(lista_planetas)):
		if planeta==lista_planetas[i]:
			print(f"velocidad de escape {velocidad_escape[i]}")

if __name__ == '__main__': # punto de entrada
	run()
