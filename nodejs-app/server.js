const express = require('express');
const bodyParser = require('body-parser');
const pgp = require('pg-promise')();
const app = express();
const port = process.env.PORT || 3000;

// PostgreSQL database configuration
const db = pgp({
  user: 'your-db-user',
  password: 'your-db-password',
  host: 'your-db-host',
  port: 5432, // PostgreSQL default port
  database: 'your-db-name',
});

// Middleware for parsing JSON requests
app.use(bodyParser.json());

// Define a route to get all items from the database
app.get('/api/items', async (req, res) => {
  try {
    const items = await db.any('SELECT * FROM items');
    res.json(items);
  } catch (error) {
    console.error('Error fetching items:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Define a route to add a new item to the database
app.post('/api/items', async (req, res) => {
  const { name, description } = req.body;

  try {
    const newItem = await db.one(
      'INSERT INTO items(name, description) VALUES($1, $2) RETURNING *',
      [name, description]
    );
    res.status(201).json(newItem);
  } catch (error) {
    console.error('Error adding item:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
