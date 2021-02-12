const mix = require('laravel-mix');


let staticPath = "app/static/build";
let resourcesPath = "app/resources";

mix.setResourceRoot("/static/build"); // setResroucesRoots add prefix to url() in scss on example: from /images/close.svg to /static/images/close.svg
mix.setPublicPath("app/static"); // Path where mix-manifest.json is created

// if you don't need browser-sync feature you can remove this lines
if (process.argv.includes("--browser-sync")) {
  mix.browserSync("localhost:8000");
}
mix.webpackConfig({
  module: {
    rules: [
      {
        test: /\.html$/,
        loader: 'vue-template-loader',

        // We don't want to pass `src/index.html` file to this loader.
        exclude: /index.html/,
        options: {
          transformToRequire: {
            img: 'src'
          }
        }
      }
    ]
  }
})

// Now you can use full mix api
// Refer the file that was created in Step 2 to be compile
mix.js(`${resourcesPath}/js/app.js`, `${staticPath}/`).vue();
mix.sass(`${resourcesPath}/sass/app.scss`, `${staticPath}/`);