class_name DatosInteractuables

const CUARTO_UMA: Dictionary = {
	Vector2i(30, 19): {"tipo": "dialogo", "texto": "La cama de Uma. Tiene tres almohadas porque dos siempre terminan en el piso.", },
	Vector2i(30, 18): {"tipo": "dialogo", "texto": "La cama de Uma. Tiene tres almohadas porque dos siempre terminan en el piso."},
	Vector2i(20, 10): {"tipo": "mesaCuartoUma", "texto": "Mesa de estudio, no tengo tarea hoy."},
	Vector2i(20, 37): {"tipo": "perchero", "texto": "Algunas cosas simplemente dejan de usarse."},
	Vector2i(20, 20): {"tipo": "armario", "texto": "Podría cambiarme… pero estoy bien así."},
	Vector2i(26, 51): {"tipo": "espejo", "texto": "Que lindos ojazos... Dio mio."},
	Vector2i(22, 54): {"tipo": "objetos", "texto": "Mesa de objetos"},
	
	Vector2i(5, 32): {"tipo": "puerta", "destino": "res://scenes/world/sala.tscn"},
}

const PASILLO: Dictionary ={
	Vector2i(26, 22): {"tipo": "puerta", "destino": "res://scenes/world/CuartoUma.tscn"},
	}

const ZONA_CALLE: Dictionary = {
	# Vector2i(x, y): {"tipo": "...", ...},
}

const MERCADO_VIEJO: Dictionary = {
	# Vector2i(x, y): {"tipo": "...", ...},
}

const PARQUE_RIBERENO: Dictionary = {
	# Vector2i(x, y): {"tipo": "...", ...},
}
