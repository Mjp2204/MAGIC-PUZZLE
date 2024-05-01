# MAGIC PUZZLE 

## Introduccion
Bienvenido a Magic Puzzle

¡Prepárate para un desafío divertido y lleno de magia! En Magic Puzzle, te embarcarás en un viaje emocionante mientras resuelves puzzles y desbloqueas secretos en un mundo lleno de misterio y encanto.

### Objetivo del juego:
Tu objetivo es reorganizar las imágenes dentro de un cuadrado mágico para restaurar el orden correcto. Cada cuadrado está dividido en una cuadrícula de celdas, y tendrás que mover las imágenes dentro de estas celdas para resolver el puzzle.

### Cómo jugar:

Usa las flechas de tu teclado para mover las imágenes dentro del cuadrado mágico. Las flechas izquierda y derecha te permiten mover las imágenes horizontalmente, mientras que las flechas arriba y abajo te permiten moverlas verticalmente.
Presta atención a tus movimientos, ya que cada uno cuenta. ¡Intenta resolver el puzzle con la menor cantidad de movimientos posible para obtener la mejor puntuación!
### Características del juego:

- Desafíos aleatorios: Cada vez que juegues, las imágenes dentro del cuadrado mágico se reorganizarán de forma aleatoria, lo que garantiza una experiencia única en cada partida.
Música mágica: Sumérgete en el mundo encantado de Magic Puzzle con una banda sonora cautivadora que te acompañará en tu viaje.
- Gráficos asombrosos: Disfruta de hermosos gráficos y animaciones que dan vida al mundo del juego.

¡Prepárate para una aventura llena de diversión y sorpresas en Magic Puzzle! ¿Tienes lo que se necesita para resolver todos los puzzles y descubrir los secretos ocultos dentro del cuadrado mágico? ¡Atrévete a descubrirlo!

![Inicio_juego](<IMAGENES/MAGIC PUZZLE.png>)

## Diagramas:
### Diagrama secuencias:
El diagrama de secuencia que se presenta a continuación representa la interacción entre los distintos componentes del juego "Magic Puzzle". Este juego desafía a los jugadores a mover fichas dentro de un cuadrado para alcanzar un estado de orden específico y ganar la partida.

El juego comienza con la iniciativa del jugador, quien inicia el juego a través de la interfaz de usuario. A medida que el jugador realiza movimientos, el juego procesa estas acciones y actualiza la disposición de las fichas en el cuadrado. El diagrama ilustra claramente cómo se manejan estas interacciones entre el jugador, el juego y el cuadrado de fichas.

El objetivo final del juego es alcanzar un estado específico donde todas las fichas estén en orden. Una vez que se alcanza este estado, el juego informa al jugador sobre su victoria.

A través de este diagrama de secuencia, se proporciona una visión detallada del flujo de juego y las interacciones entre los distintos elementos del juego "Magic Puzzle".

### Diagrama de casos:
El diagrama de casos de uso representa las interacciones entre los diferentes actores y las funcionalidades del juego "Magic Puzzle". Este juego desafía a los jugadores a mover fichas dentro de un cuadrado para alcanzar un estado de orden específico y ganar la partida.

El actor principal del juego es el "Jugador", quien interactúa con las diferentes funcionalidades del juego a través de una interfaz de usuario.

El juego se inicia cuando el jugador selecciona la opción "Iniciar Juego". Una vez que se inicia el juego, el jugador puede realizar movimientos de cuadrículas para reorganizar las fichas dentro del cuadrado. Después de cada movimiento, el juego verifica si se ha alcanzado el estado de orden correcto. Si el estado es correcto, el juego muestra un mensaje de victoria al jugador; de lo contrario, continúa permitiendo al jugador realizar movimientos hasta que se alcance el estado correcto.

A través de este diagrama de casos de uso, se proporciona una visión clara de las interacciones entre el jugador y las diferentes funcionalidades del juego "Magic Puzzle".

### Diagrama de clases:
El diagrama de clases representa la estructura y las relaciones entre los diferentes componentes de la lógica del juego "Magic Puzzle". Este juego desafía a los jugadores a mover fichas dentro de un cuadrado para alcanzar un estado de orden específico y ganar la partida.

El paquete "Logica" contiene los elementos principales relacionados con la lógica del juego. La interfaz "Pantalla" define los métodos comunes para mostrar y dibujar en la pantalla del juego. La clase "Cuadros" representa el cuadrado de fichas del juego, que contiene una matriz de imágenes representando las fichas y realiza las operaciones de movimiento y manipulación de fichas.

La clase "Cuadros" contiene métodos para cargar imágenes, procesar movimientos (hacia arriba, abajo, izquierda, derecha), dibujar el cuadrado en la pantalla, así como para obtener la posición vacía en el cuadrado y realizar intercambios de imágenes cuando se realizan movimientos.

La relación entre "Pantalla" y "Cuadros" indica que la pantalla del juego utiliza la funcionalidad proporcionada por la clase "Cuadros" para mostrar y dibujar el estado actual del cuadrado de fichas.

A través de este diagrama de clases, se proporciona una visión clara de la estructura y las responsabilidades de los componentes de la lógica del juego "Magic Puzzle".


## Autor
- Maria Jose Patiño Vera 20232020053