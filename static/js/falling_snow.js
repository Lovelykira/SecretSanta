function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function getRandomBool() {
    return (getRandomInt(0, 100) % 2 == 0)
}

// Тип данных, представляющий отдельный мячик
function Flake(x, y, dx, dy, size, speed, opacity) {
    this.x = x;
    this.y = y;
    this.dx = dx;
    this.dy = dy;
    this.size = size;
    this.src = '/static/js/img/snow.png';
    this.speed = speed;
    this.opacity = opacity;
    this.image = new Image(); //МЕНЯЛ ТУ
    this.image.src = this.src; //МЕНЯЛ ТУ
}

// Массив, содержащий информацию обо всех мячиках на холсте
var flakes = [];


function addFlake() {

    // Создаем новый мячик
    var x_pos = getRandomInt(0, canvas.width),
        y_pos = getRandomInt(0, canvas.height * 0.1),
        dx = getRandomInt(0, 5),
        dy = getRandomInt(3, 6),
        speed = getRandomInt(1, 20),
        size = getRandomInt(10, 40),
        opacity = getRandomInt(10, 80);

    var flake = new Flake(x_pos, y_pos, dx, dy, size, speed, opacity / 100);

    // Сохраняем его в массиве
    flakes.push(flake);
}

function clearFlakes() {
    // Удаляем все мячики
    flakes = [];
}


function load_fakes() {
    // Определение контекста рисования
    canvas = document.getElementById("drawingCanvas");
    context = canvas.getContext("2d");

    // Обновляем холст через 0.02 секунды
    setTimeout("drawFrame()", 100);
};


function drawFrame() {

    context.clearRect(0, 0, canvas.width, canvas.height);
    addFlake();

    // Вызываем метод beginPath(), чтобы убедиться,
    // что мы не рисуем часть уже нарисованного содержимого холста
    context.beginPath();

    // Перебираем все мячики
    for (var i = 0; i < flakes.length; i++) {

        // Перемещаем каждый мячик в его новую позицию
        (function () {
            var flake = flakes[i];
            flake.x += flake.dx;
            flake.y += flake.dy;
            if (flake.x > canvas.width || flake.y > canvas.height) {
                a = flakes.splice(i, 1);
            }
            context.drawImage(flake.image, flake.x, flake.y, flake.size, flake.size)  //МЕНЯЛ ТУТ
        })(i);
    }
    context.closePath();  //МЕНЯЛ ТУТ

    // Рисуем следующий кадр через 40 миллисекунд
    setTimeout("drawFrame()", 40); //МЕНЯЛ ТУТ
}