extends Node2D

func _ready() -> void:
	pass

func _on_btn_jugar_pressed() -> void:
	if SaveManager.hay_partida():
		var escena = SaveManager.get_jugador("escena_actual")
		Transition.play(escena)
		print(escena)
		print("DEBUG: jugador en", escena)
	else:
		Transition.play("res://scenes/world/CuartoUma.tscn", 1.0)

func _on_btn_opciones_pressed() -> void:
	Ajustes.abrir(false)
	
func _on_btn_salir_pressed():
	get_tree().quit()
