var config = {};

config.db = {};
// the URL shortening host - shortened URLs will be this + baseHash ID

// i.e.: http://localhost:5000/3Ys
config.webhost = ' http://localhost/';

// your MongoDB host and database name
config.db.localhost = 'mongodb://localhost/slashurl';
config.db.port = 27017;
config.db.name = 'slashurl';
config.db.collections = ['urls', 'counters'];

module.exports = config;
