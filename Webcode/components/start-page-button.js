import {
  LitElement,
  html,
} from "https://cdn.jsdelivr.net/gh/lit/dist@3/core/lit-core.min.js";

class StartPageButton extends LitElement {
  // Defining the rectColor property
  static properties = {
    rectColor: { type: String, attribute: "rect-color" },
  };

  // Provide default color if none is specified
  constructor() {
    super();
    this.rectColor = "#4E80FF"; // Default color
  }

  render() {
    return html`
      <button @click=${this.handleClick} class="button-1">
        <svg
          width="291"
          height="124"
          viewBox="0 0 291 124"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <g filter="url(#filter0_d_11_32)">
            <rect
              x="21"
              y="18"
              width="251"
              height="84"
              fill="${this.rectColor}" <!-- Using the dynamic color -->
            />
          </g>
          <defs>
            <filter
              id="filter0_d_11_32"
              x="0"
              y="0"
              width="291"
              height="124"
              filterUnits="userSpaceOnUse"
              color-interpolation-filters="sRGB"
            >
              <feFlood flood-opacity="0" result="BackgroundImageFix" />
              <feColorMatrix
                in="SourceAlpha"
                type="matrix"
                values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0"
                result="hardAlpha"
              />
              <feOffset dx="-1" dy="2" />
              <feGaussianBlur stdDeviation="10" />
              <feComposite in2="hardAlpha" operator="out" />
              <feColorMatrix
                type="matrix"
                values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.2 0"
              />
              <feBlend
                mode="normal"
                in2="BackgroundImageFix"
                result="effect1_dropShadow_11_32"
              />
              <feBlend
                mode="normal"
                in="SourceGraphic"
                in2="effect1_dropShadow_11_32"
                result="shape"
              />
            </filter>
          </defs>
        </svg>
      </button>
    `;
  }

  handleClick() {
    alert("Button clicked!");
  }
}

// Register the custom element
customElements.define("start-page-button", StartPageButton);
