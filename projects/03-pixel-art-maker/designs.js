// Select color input
let color = document.getElementById('colorPicker');
let canvas = document.getElementById('pixelCanvas');

// Select size input
let sizePicker = document.getElementById('sizePicker');

// When size is submitted by the user, call makeGrid()
sizePicker.addEventListener('submit', function (event) {
    event.preventDefault();

    if (canvas.firstElementChild !== null) {
        canvas.firstElementChild.remove();
    };

    let height = document.getElementById('inputHeight').value;
    let width = document.getElementById('inputWidth').value;

    makeGrid(height, width);
});

function colorIt(event) {
    // if statement is used to check that the target is a cell without it a bug potentially changes color of the whole canvas
    if (event.target.nodeName === 'TD') {
        event.target.style.backgroundColor = color.value;
    };
};

function makeGrid(height, width) {

    // Your code goes here!
    for (let i = 0; i < height; i++) {
        let row = canvas.insertRow(i);
        for (let j = 0; j < width; j++) {
            let cell = row.insertCell(j);
        };
    };
    // A single event handler is used to delegate events to optimize for performance
    canvas.addEventListener('click', colorIt);
};