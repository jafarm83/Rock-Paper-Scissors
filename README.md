<svg width="300" height="165" viewBox="0 0 300 165" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="descId">
  <title id="titleId">Most Used Languages</title>
  <desc id="descId">Python, PHP, HTML, CSS usage chart</desc>
  <style>
    .header {
      font: 600 18px 'Segoe UI', Ubuntu, Sans-Serif;
      fill: #fff;
      animation: fadeInAnimation 0.8s ease-in-out forwards;
    }
    .stat {
      font: 600 14px 'Segoe UI', Ubuntu, Sans-Serif;
      fill: #9f9f9f;
    }
    .lang-name {
      font: 400 11px "Segoe UI", Ubuntu, Sans-Serif;
      fill: #9f9f9f;
    }
    .stagger {
      opacity: 0;
      animation: fadeInAnimation 0.3s ease-in-out forwards;
    }
    #rect-mask rect {
      animation: slideInAnimation 1s ease-in-out forwards;
    }
    .lang-progress {
      animation: growWidthAnimation 0.6s ease-in-out forwards;
    }
    @keyframes fadeInAnimation {
      from { opacity: 0; }
      to { opacity: 1; }
    }
    @keyframes slideInAnimation {
      from { width: 0; }
      to { width: calc(100% - 100px); }
    }
    @keyframes growWidthAnimation {
      from { width: 0; }
      to { width: 100%; }
    }
  </style>

  <rect x="0.5" y="0.5" rx="4.5" height="99%" stroke="#e4e2e2" width="299" fill="#151515" stroke-opacity="1" />

  <g transform="translate(25, 35)">
    <text x="0" y="0" class="header">Most Used Languages</text>
  </g>

  <g transform="translate(0, 55)">
    <svg x="25">
      <mask id="rect-mask">
        <rect x="0" y="0" width="250" height="8" fill="white" rx="5"/>
      </mask>

      <rect mask="url(#rect-mask)" x="0" y="0" width="100" height="8" fill="#3572A5" /> <!-- Python 40% -->
      <rect mask="url(#rect-mask)" x="100" y="0" width="75" height="8" fill="#4F5D95" /> <!-- PHP 30% -->
      <rect mask="url(#rect-mask)" x="175" y="0" width="50" height="8" fill="#e34c26" /> <!-- HTML 20% -->
      <rect mask="url(#rect-mask)" x="225" y="0" width="25" height="8" fill="#563d7c" /> <!-- CSS 10% -->

      <g transform="translate(0, 25)">
        <g transform="translate(0, 0)">
          <g class="stagger" style="animation-delay: 450ms">
            <circle cx="5" cy="6" r="5" fill="#3572A5" />
            <text x="15" y="10" class="lang-name">Python 40%</text>
          </g>
        </g>
        <g transform="translate(0, 25)">
          <g class="stagger" style="animation-delay: 600ms">
            <circle cx="5" cy="6" r="5" fill="#4F5D95" />
            <text x="15" y="10" class="lang-name">PHP 30%</text>
          </g>
        </g>
        <g transform="translate(0, 50)">
          <g class="stagger" style="animation-delay: 750ms">
            <circle cx="5" cy="6" r="5" fill="#e34c26" />
            <text x="15" y="10" class="lang-name">HTML 20%</text>
          </g>
        </g>
      </g>

      <g transform="translate(150, 25)">
        <g transform="translate(0, 0)">
          <g class="stagger" style="animation-delay: 900ms">
            <circle cx="5" cy="6" r="5" fill="#563d7c" />
            <text x="15" y="10" class="lang-name">CSS 10%</text>
          </g>
        </g>
      </g>
    </svg>
  </g>
</svg>
