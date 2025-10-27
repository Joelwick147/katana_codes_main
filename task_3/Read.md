#Ball Following Pointer or Screen Touch

This is a simple HTML, CSS, and JavaScript code snippet that creates a ball element that follows the mouse pointer on a desktop or screen touch on a mobile device. It also leaves a faint trace behind as it moves.

## Features

- Ball follows mouse pointer or screen touch.
- Leaves a subtle trace behind.
- Responsive design for different screen sizes.
- Smooth movement transition.

## How to Use

1.  Save the code as an `.html` file (e.g., `index.html`).
2.  Open the `.html` file in a web browser.
3.  Move your mouse or touch the screen to see the ball follow.

## Code Explanation

### HTML

The HTML structure is simple, with a `div` element with the ID `ball` representing the ball.

### CSS

The CSS styles the ball, the body, and the trace elements:

- `#ball`: Styles the ball with a circular shape, background color, positioning, and a subtle box shadow.
- `body`: Sets the body's margin, height, overflow, and a subtle background for the trace effect.
- `.trace`: Styles the trace elements with a smaller circular shape, a faint background color with transparency, and a fade-out transition.

### JavaScript

The JavaScript handles the ball's movement and trace creation:

- `moveBall(x, y)`: This function creates a new trace element at the specified `x` and `y` coordinates, appends it to the body, and then fades it out and removes it after a short delay. It also updates the position of the main ball element.
- `mousemove` event listener: Calls `moveBall` when the mouse moves, adjusting the coordinates to center the ball on the cursor.
- `touchmove` event listener: Calls `moveBall` when a touch move occurs on a mobile device, preventing default scrolling behavior and adjusting the coordinates for the touch point.
- `click` event listener: Calls `moveBall` when the screen is tapped, allowing the ball to appear at the tap location.
- `load` event listener: Calls `moveBall` when the window loads to position the ball initially in the center of the screen.
