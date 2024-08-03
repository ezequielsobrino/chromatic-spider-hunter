# Chromatic Spider: Color Hunter

A colorful and interactive game developed using Python and Pygame, featuring a procedurally animated spider that hunts for vibrant color orbs.

## Table of Contents
- [Quick Start](#quick-start)
- [How to Play](#how-to-play)
- [Controls](#controls)
- [Development Process with Claude](#development-process-with-claude)
- [Chat References](#chat-references)
- [Future Improvements](#future-improvements)
- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)

## Quick Start

1. Ensure you have Python installed on your system.
2. Clone the repository and install the requirements (see [Installation](#installation)).
3. Run the game using:
   ```
   python chromatic_spider_game.py
   ```

## How to Play

- Click anywhere on the screen to move the spider.
- Catch as many color orbs as possible to increase your score.
- Each level lasts 60 seconds.
- The game becomes more challenging as you progress through levels.

## Controls

- Mouse click: Move the spider to the clicked location.
- Close window or press 'Q' to quit the game.

## Development Process with Claude

The development of the Chromatic Spider game, particularly the procedural animation of the spider, was assisted by Claude, an AI language model. Here's a brief summary of how Claude was utilized:

1. **Initial Concept**: Claude provided guidance on setting up a basic Pygame project and implementing a simple spider character with basic movement.

2. **Procedural Animation**: Claude offered suggestions for creating the spider's leg animations using trigonometric functions, helping to achieve a natural, crawling motion.

3. **Movement Mechanics**: When faced with issues like circular movement, Claude provided solutions to implement smooth, direct movement towards clicked points.

4. **Visual Enhancements**: Claude suggested improvements such as adding a body wobble effect, creating jointed leg segments, and implementing a color-changing effect for the spider.

5. **Game Mechanics**: Claude assisted in developing the color orb catching mechanic, scoring system, and level progression.

6. **Code Structure**: Throughout the process, Claude provided advice on code organization and object-oriented design principles to keep the project maintainable.

7. **Debugging**: Claude offered debugging strategies and helped interpret error messages when issues arose during development.

By iteratively providing code snippets, explaining concepts, and offering solutions to specific problems, Claude played a crucial role in the development of this game, particularly in achieving the smooth, procedural animation of the spider character.

## Chat References

For those interested in exploring the development process in more detail, here are references to the chats with Claude that contributed to this project:

1. [Exploring Pygame, the Python Game Development Library](https://claude.site/artifacts/7afe76b1-68ba-46aa-a1e1-9abf61331be4)
2. [Adjusting Spider Leg Behavior](https://claude.site/artifacts/96fa8b48-e491-4082-9574-02ad0b5df074)
3. [Improving Spider Animation](https://claude.site/artifacts/55da098d-8c73-4294-8424-bf95c4d1be0b)

These chats provide insights into the step-by-step development process, problem-solving approaches, and the evolution of the game's features.

## Future Improvements

- Add obstacles or terrain that affects movement.
- Implement different spider species with unique movement patterns.
- Enhance graphics with textures and shadows for increased realism.

## Installation

To set up the project locally, follow these steps:

1. Ensure you have Python 3.x installed on your system.
2. Clone the repository:
   ```
   git clone https://github.com/ezequielsobrino/chromatic-spider-hunter.git
   ```
3. Navigate to the project directory:
   ```
   cd chromatic-spider-game
   ```
4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Run the game:
   ```
   python chromatic_spider_game.py
   ```

## Contributing

Contributions to the Chromatic Spider: Color Hunter project are welcome! Here's how you can contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-branch-name`.
5. Submit a pull request.

Please make sure to update tests as appropriate and adhere to the project's coding standards.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to contribute to the project or use it as a basis for your own game development experiments!