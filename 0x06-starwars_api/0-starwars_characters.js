#!/usr/bin/node
// // A program that takes in a movie id from the command line argument
// // and print the characters of that movie.

// const request = require('request');

// let movieId = NaN;
// if (process.argv.length > 2) {
//   movieId = Number(process.argv[2]);
//   if (isNaN(movieId)) {
//     console.log('movie_id must be a number not a string');
//     process.exit(1);
//   }
// } else {
//   console.log('Usage: 0-starwars_characters.js <movie_id>');
//   process.exit(1);
// }

// const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// function getUrl (url) {
//   const promise = new Promise((resolve, reject) => {
//     request(url, (err, res, body) => {
//       if (err) {
//         reject(err);
//       }
//       resolve(JSON.parse(body));
//     });
//   });
//   return promise;
// }

// getUrl(movieUrl).then(body => {
//   const characters = body.characters;
//   characters.forEach(characterUrl => {
//     getUrl(characterUrl).then(resp => {
//       console.log(resp.name);
//     });
//   });
// }).catch(err => {
//   console.log(err);
// });

// #!/usr/bin/node
// A program that takes in a movie id from the command line argument
// and print the characters of that movie.

const request = require('request');

let movieId = NaN;
if (process.argv.length > 2) {
  movieId = Number(process.argv[2]);
  if (isNaN(movieId)) {
    console.log('movie_id must be a number not a string');
    process.exit(1);
  }
} else {
  console.log('Usage: 0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

function getUrl (url) {
  const promise = new Promise((resolve, reject) => {
    request(url, (err, res, body) => {
      if (err) {
        reject(err);
      }
      resolve(JSON.parse(body));
    });
  });
  return promise;
}

getUrl(movieUrl).then(body => {
  const characters = body.characters;
  const charBody = [];
  characters.forEach(characterUrl => {
    charBody.push(getUrl(characterUrl));
  });
  return Promise.all(charBody);
}).then((charPromises) => {
  charPromises.forEach(char => {
    console.log(char.name);
  });
}).catch(err => {
  console.log(err);
});
