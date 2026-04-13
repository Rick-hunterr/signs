extends CanvasLayer

signal enviar_joystick(j: Joystick)
signal boton_interactuar_presionado
signal boton_direccion_presionado(dir: Vector2)
signal boton_direccion_soltado

@onready var joystick      = $Control/Control/Joystick
@onready var gamepad       = $Control/BtnsDireccionales
@onready var btn_interactuar = $Control/Control2/BtnInteractuar
@onready var btn_arriba    = $Control/BtnsDireccionales/BtnArriba
@onready var btn_abajo     = $Control/BtnsDireccionales/BtnAbajo
@onready var btn_izquierda = $Control/BtnsDireccionales/BtnIzquierda
@onready var btn_derecha   = $Control/BtnsDireccionales/BtnDerecha
var ultimo_control: String = ""

var puede_usar = true
	

func _ready() -> void:
	var player = get_tree().get_first_node_in_group("uma")

	if player:
		enviar_joystick.connect(player.recibir_joystick)
	
	enviar_joystick.emit(joystick)
	btn_interactuar.pressed.connect(_on_btn_interactuar_pressed)
	btn_arriba.button_down.connect(func(): boton_direccion_presionado.emit(Vector2.UP))
	btn_abajo.button_down.connect(func(): boton_direccion_presionado.emit(Vector2.DOWN))
	btn_izquierda.button_down.connect(func(): boton_direccion_presionado.emit(Vector2.LEFT))
	btn_derecha.button_down.connect(func(): boton_direccion_presionado.emit(Vector2.RIGHT))
	btn_arriba.button_up.connect(func(): boton_direccion_soltado.emit())
	btn_abajo.button_up.connect(func(): boton_direccion_soltado.emit())
	btn_izquierda.button_up.connect(func(): boton_direccion_soltado.emit())
	btn_derecha.button_up.connect(func(): boton_direccion_soltado.emit())
	actualizar_control()

func _on_btn_interactuar_pressed() -> void:
	if not puede_usar:
		return
	puede_usar = false
	boton_interactuar_presionado.emit()
	await get_tree().create_timer(1.0).timeout
	puede_usar = true

func _on_touch_screen_button_pressed() -> void:
	Ajustes.abrir(true)

func _process(_delta: float) -> void:
	var control_actual = SaveManager.get_ajuste("tipo_control")
	if control_actual != ultimo_control:
		ultimo_control = control_actual
		_aplicar_visibilidad(control_actual)

func _aplicar_visibilidad(tipo: String) -> void:
	var es_joystick = tipo == "joystick"
	joystick.visible = es_joystick
	gamepad.visible  = not es_joystick
	if not es_joystick and joystick != null:
		joystick.index = -1
		joystick.direccion = Vector2.ZERO
		joystick.distancia = 0.0
		joystick.punto.position = Vector2.ZERO

func actualizar_control() -> void:
	var uma = get_tree().get_first_node_in_group("player")
	if uma:
		uma.resetear_control()
