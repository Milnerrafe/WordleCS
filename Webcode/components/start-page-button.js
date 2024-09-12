import {
  LitElement,
  html,
  css,
} from "https://cdn.jsdelivr.net/gh/lit/dist@3/core/lit-core.min.js";

class StartButton extends LitElement {
  static properties = {
    rectColor: { type: String, attribute: "rect-color" },
    hoverColor: { type: String, attribute: "hover-color" },
    buttonText: { type: String, attribute: "button-text" },
  };

  constructor() {
    super();
    this.rectColor = "#4E80FF"; // Default color
    this.hoverColor = "#3B6ADF"; // Default hover color
    this.buttonText = "Click Me!"; // Default button text
  }

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

  handleClick() {
    if (this.buttonText == "Play Random") {
      window.location.href = "/play";
    } else if (this.buttonText == "How to Play") {
      window.location.href = "/how-to-play";
    } else if (this.buttonText == "Close Game") {
      window.close();
    } else {
      if (typeof this.buttonText === "string") {
        console.error("The Button was clicked with a Unrecognised value of");
        console.error(this.buttonText);
      } else {
        console.error("The Button was clicked with no value");
      }
    }
  }
}

// Register the custom element
customElements.define("start-page-button", StartButton);
