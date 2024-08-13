<h1>Pacman</h1>

<h2>Overview</h2>

This project is a simple implementation of the classic Pacman game, developed as an educational tool to help understand and apply various Data Structures and Algorithms (DSA). The game is built using Python and is designed to demonstrate the practical use of algorithms in a fun and interactive way.

<h2>Features</h2>

<ul>
  <li><strong>Classic Pacman Gameplay:</strong> Navigate the maze, eat all the dots, and avoid the ghosts.</li>
  <li>
    <strong>Algorithmic Challenges:</strong> Different levels are designed to teach and apply various algorithms, such as:
    <ul>
      <li><strong>Pathfinding Algorithms:</strong> Implement and visualize algorithms like BFS, DFS, A* in real-time as Pacman finds his way through the maze.</li>
      <li><strong>Data Structures:</strong> Utilize stacks, queues, priority queues, and more to manage game states and AI decisions.</li>
      <li><strong>Graph Theory:</strong> Represent the maze as a graph and explore graph traversal techniques.</li>
    </ul>
  </li>
  <li><strong>Educational Mode:</strong> Step through the algorithms used in the game with detailed explanations and visual aids.</li>
  <li><strong>Customizable Levels:</strong> Create your own maze layouts and challenges to explore different algorithms.</li>
</ul>

<h2>Tech Stack</h2>

<ul>
  <li>Language: Python</li>
  <li>Libraries:</li>
  <ul>
    <li>`<strong>pygame</strong>` for game development and visualization.</li>
    <li>`<strong>numpy</strong>` and `<strong>networkx</strong>` for data structures and algorithm implementations.</li>
  </ul>
  
</ul>

<h2>Installation</h2>

To set up and run the Pacman game on your local machine, follow these steps:

<h3>Prerequisites</h3>
Make sure you have Python installed. You can download it ZIP file or fork repo.

<h3>Setup</h3>

1. Clone the repository:

	`git clone https://github.com/yourusername/pacman-dsa.git`

2. Navigate to the project directory:

	`cd pacman-dsa`

3. Install required dependencies:

	`pip install -r requirements.txt`

4. Run the game:

	`python main.py`


<h2>How to Play</h2>
<ul>
  <li><strong>Movement:</strong> Use the arrow keys to move Pacman through the maze.</li>
  <li><strong>Objective:</strong> Eat all the dots in the maze while avoiding ghosts.</li>
  <li><strong>Educational Mode:</strong> Activate educational mode from the main menu to step through the algorithms used in real-time.</li>
</ul>


<h2>Learning Objectives</h2>
This project is designed to help you learn and apply the following DSA concepts:

1. <strong>Pathfinding Algorithms: </strong>Understand and implement BFS, DFS, and A* algorithms in a practical context.
2. <strong>Data Structures: </strong>Use stacks, queues, and priority queues to manage game logic.
3. <strong>Graph Representation: </strong>Learn how to represent the game maze as a graph and apply graph traversal techniques.
4. <strong>Algorithm Optimization: </strong>Explore ways to optimize algorithms for real-time gameplay.

<h2>Customization</h2>
To create custom levels or challenges:

1. Edit the `levels.py` file in the src directory.
2. Define new maze layouts using 2D arrays.
3. Customize the behavior of ghosts and other game elements in the `game_logic.py` file.
