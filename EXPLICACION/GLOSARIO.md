## ¿Frame?
Un frame en un videojuego representa la imagen, el sonido y cualquier otro efecto visual o auditivo que se debe mostrar en un instante específico del juego. Puedo pensar en un frame como un cuadro individual en una línea de tiempo que muestra todo el entorno del juego en un momento dado.

En un juego, se actualiza y renderiza un nuevo frame en cada iteración del bucle principal del juego. Este bucle se ejecuta continuamente a una velocidad determinada, generalmente medida en frames por segundo (FPS). Cada frame muestra una instantánea de la escena del juego en ese momento particular.

Cada frame contiene la información necesaria para representar gráficamente los elementos del juego, como los personajes, los objetos, el fondo, los efectos especiales, la interfaz de usuario, entre otros. Además, también puede incluir los efectos de sonido y música correspondientes a ese instante específico del juego.

La combinación de todos estos frames, renderizados y reproducidos a una velocidad constante, crea la ilusión de movimiento y acción continua en el juego. Por lo tanto, los frames en conjunto forman la secuencia de imágenes y sonidos que se perciben como una experiencia de juego dinámica y fluida.

## def events(self):

Este metodo maneja los eventos del juego, en Pygame, los eventos son objetos que representan acciones o sucesos que ocurren durante la ejecución de un juego o una aplicación. Estos eventos pueden ser generados por diferentes fuentes, como el teclado, el mouse, el sistema operativo u otros dispositivos de entrada.

La función pygame.event.get() se utiliza para obtener una lista de todos los eventos que han ocurrido desde la última vez que se llamó a esta función. Cada evento en la lista es un objeto que contiene información sobre el tipo de evento y cualquier dato adicional asociado.

Algunos ejemplos comunes de eventos que pueden ser capturados con pygame.event.get() incluyen:

#### Eventos de teclado:
Representan las pulsaciones de teclas o la liberación de teclas en el teclado.
Eventos de ratón: Representan los movimientos del cursor del ratón, los clics de los botones del ratón o la rueda del ratón.
#### Eventos de ventana: 
Representan cambios en el tamaño, posición o estado de la ventana del juego, como minimizar, maximizar o cerrar la ventana.
Eventos de tiempo: Representan eventos basados en el tiempo, como la generación de un temporizador o un reloj interno del juego.

#### Eventos de ratón: 
Estos eventos se generan cuando se realiza alguna acción con el ratón, como moverlo, hacer clic con los botones del ratón o desplazar la rueda del ratón. Puedes utilizar eventos de ratón para controlar la interacción del usuario con elementos del juego.

#### Eventos de tiempo: 
Pygame también puede generar eventos basados en el tiempo, como la generación de un temporizador o un reloj interno. Puedes utilizar estos eventos para controlar la lógica del juego que depende del tiempo, como la animación, la generación de enemigos o la actualización de eventos periódicos.

#### Eventos personalizados: 
Puedes definir tus propios eventos personalizados para comunicar y controlar diferentes partes de tu juego.
Al capturar y procesar los eventos, puedes escribir lógica de juego basada en las acciones del usuario o en los cambios en el entorno del juego. Por ejemplo, puedes mover un personaje cuando se presiona una tecla específica, realizar una acción cuando se hace clic en un objeto o responder a eventos de ventana para ajustar el comportamiento del juego.

La función pygame.event.get() devuelve una lista de eventos pendientes en el orden en que ocurrieron, y vacía la cola de eventos para el siguiente procesamiento.

## draw_background()
El método draw_background() es un método personalizado que se utiliza para dibujar el fondo en la pantalla de un juego o aplicación. El propósito específico y la implementación del método pueden variar dependiendo del juego en particular.

En general, el método draw_background() se encarga de realizar las operaciones necesarias para dibujar el fondo en la pantalla de juego. Esto puede incluir dibujar imágenes, formas geométricas, patrones o cualquier otro elemento visual que forme el fondo de la escena del juego.

## pygame.transform.scale
La función pygame.transform.scale() se utiliza para redimensionar una imagen o superficie en Pygame. Permite cambiar el tamaño de una imagen para ajustarse a dimensiones específicas. En el codigo vamos le pasamos como primer paramatro la imagen como fondo de la pantalla y despues le pasamos las constantes que es son el tamaño de la pantalla

## self.screen.blit
El método blit() se utiliza en Pygame para dibujar una imagen o superficie en otra superficie. Es una abreviatura de "block transfer" y se utiliza comúnmente para copiar una imagen o parte de ella en una ventana o pantalla de juego.

## pygame.display.update() y pygame.display.flip()

Tanto game.display.update() como pygame.display.flip() se utilizan para actualizar la ventana o pantalla y mostrar los cambios realizados en los gráficos o en la interfaz del juego. Sin embargo, hay algunas diferencias sutiles entre las dos.

#### pygame.display.update():
 Se utiliza para actualizar áreas específicas de la pantalla. Puedes pasarle argumentos opcionales para indicar qué partes de la pantalla deben actualizarse. Por ejemplo, si tienes una animación en una parte específica de la pantalla y solo quieres actualizar esa área en cada iteración del bucle del juego, puedes pasar un rectángulo que represente esa área a pygame.display.update(). Esto puede ayudar a mejorar el rendimiento al evitar actualizar la pantalla completa si solo hay cambios en una parte de ella.

 #### pygame.display.flip():
 Es una función que se utiliza para actualizar toda la ventana o pantalla de juego. Después de realizar cualquier cambio en los gráficos o en la interfaz del juego, llamar a pygame.display.flip() es necesario para que los cambios se muestren en la pantalla.

Cuando se llama a pygame.display.flip(), todos los cambios que se hayan realizado en la ventana o superficie de juego se hacen visibles para el jugador. Esto implica que cualquier dibujo, imagen, texto u otro elemento gráfico que hayas agregado o modificado en la superficie de la pantalla se mostrará de manera instantánea.

#### Sprite

En Pygame, un sprite es un objeto gráfico o visual que puede ser representado en una pantalla o ventana de juego. Es una entidad visual que puede tener propiedades como posición, tamaño, imagen y comportamiento específico.

La clase Sprite en Pygame proporciona una forma conveniente de definir y manejar sprites en un juego. Al heredar de la clase Sprite, puedes crear tus propios sprites personalizados con funcionalidades específicas.

Los sprites en Pygame son ampliamente utilizados para representar personajes, enemigos, objetos, efectos visuales y otros elementos visuales en un juego. Los sprites permiten una gestión más eficiente de los elementos gráficos y facilitan la detección de colisiones y la interacción entre los diferentes elementos del juego.

Al utilizar la clase Sprite de Pygame, puedes definir métodos para actualizar y dibujar los sprites, así como para manejar eventos y colisiones. Esto facilita la creación de juegos con una mayor organización y modularidad en el código.


#### rect
En Pygame, rect es un término que se refiere a un objeto Rectángulo (Rectangle). Un rectángulo es una estructura de datos utilizada para representar un área rectangular en una pantalla o superficie de juego.

El objeto Rectángulo (pygame.Rect) en Pygame se utiliza ampliamente para realizar operaciones relacionadas con la posición, tamaño y colisiones de elementos gráficos. Proporciona atributos y métodos para manipular y acceder a las propiedades de un rectángulo, como la posición (coordenadas x e y), el tamaño (ancho y alto), entre otros.

El objeto pygame.Rect te proporciona información sobre la ubicación y el tamaño de un rectángulo en la pantalla o superficie de juego.

El objeto pygame.Rect tiene atributos como x y y, que representan las coordenadas de la esquina superior izquierda del rectángulo. Estas coordenadas indican la posición del rectángulo en relación con el sistema de coordenadas de la pantalla o superficie en la que se encuentra.

Además, pygame.Rect tiene atributos como width (ancho) y height (altura), que especifican las dimensiones del rectángulo. Estos valores te permiten determinar el tamaño del rectángulo en píxeles.

Con el objeto pygame.Rect, puedes realizar varias operaciones, como mover el rectángulo a una nueva posición, modificar su tamaño, obtener información sobre sus bordes y centro, y realizar colisiones con otros rectángulos.

#### pygame.key.get_pressed()

La función pygame.key.get_pressed() es una función de Pygame que devuelve el estado actual de todas las teclas del teclado en un arreglo de booleanos.

Cuando llamas a pygame.key.get_pressed(), esta función verifica el estado de todas las teclas del teclado y devuelve un arreglo donde cada índice corresponde a un código de tecla específico y el valor en ese índice indica si la tecla está siendo presionada (True) o no (False).