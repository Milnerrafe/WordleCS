// This JavaScript file uses a lit. Lit is a powerful JavaScript framework that helps us use web components, which is a standard for creating custom HTML components in a simple and easy to use way.
import {
  LitElement,
  html,
  css,
} from "https://cdn.jsdelivr.net/gh/lit/dist@3/core/lit-core.min.js";

// In this part of the code we are defining what attributes will be able to be put into the HTML when the component is used.
class StartButton extends LitElement {
  static properties = {
    rectColor: { type: String, attribute: "rect-color" },
    hoverColor: { type: String, attribute: "hover-color" },
    buttonText: { type: String, attribute: "button-text" },
  };

  // Here we define the default attributes in case the HTML doesn't provide any for us.
  constructor() {
    super();
    this.rectColor = "#4E80FF"; // Default color
    this.hoverColor = "#3B6ADF"; // Default hover color
    this.buttonText = "Click Me!"; // Default button text
  }
  // Here we define the CSS, or cascading style sheets. When we use lit, we don't have to worry about cascading style sheets though, because we use something called the shadow DOM, which takes the component into their own separate DOM, meaning that styles don't cascade down onto them. The CSS only applies to the elements which it renders, and no other CSS applies to it. This CSS defines how the button should look.
  static styles = css`
    .start-button {
      width: 251px;
      height: 84px;
      background-color: var(--rect-color);
      color: white;
      font-family: "Tilt Warp", sans-serif;
      font-size: 36px;
      line-height: auto;
      letter-spacing: -0.1em; /* -10% */
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      box-shadow: -1px 2px 10px rgba(0, 0, 0, 0.2); /* Shadow effect */
      transition: background-color 0.3s ease;
    }

    .start-button:hover {
      background-color: var(--hover-color);
    }
  `;

  // Here we combine the variables and the HTML that we want to render. This JavaScript also returns a finished component to the HTML to display on the screen.
  render() {
    return html`
      <div
        class="start-button"
        style="--rect-color: ${this.rectColor}; --hover-color: ${this
          .hoverColor};"
        @click=${this.handleClick}
      >
        ${this.buttonText}
      </div>
    `;
  }

  // This code is where we add the logic to the button. When the button is clicked, depending on its name provided in the HTML, it will go to different parts of the application. If the value of the button is unrecognised, we throw an error that can be viewed in the developer console on a browser. This helps us identify errors and problems.
  handleClick() {
    if (this.buttonText == "Play Random") {
      window.location.href = "/play";
    } else if (this.buttonText == "How to Play") {
      window.location.href = "/how-to-play";
    } else if (this.buttonText == "Close Game") {
      window.location.href = "/";
      window.close();
    } else {
      console.error(
        'The Button was clicked with a Unrecognised value of "' +
          this.buttonText +
          '"',
      );
    }
  }
}

// This piece of JavaScript defines the element. So, when the JavaScript file is imported into an HTML file, and somebody calls or puts down the element in the HTML file, the HTML browser knows to render this component.
customElements.define("start-page-button", StartButton);
