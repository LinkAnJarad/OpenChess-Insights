# OpenChess: Insights (Beta)

Updates:
- Roast mode feature for harsher reviews on inaccuracies, mistakes, and blunders!

- Improved ELO/rating estimation formula



An open-source chess analysis web app runnable in your local machine powered by Stockfish 16 NNUE. Includes:
- move explanations in plain language similar to chess.com's game review
- more metric functionalities than your just the eval bar: tension, control, development, and mobility
- accuracy and estimated ELO calculations
- move classifications: excellent, good, inaccuracies, mistakes, blunders, and *brilliant* moves

<video controls>
  <source src="preview.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>

**Ease-of-use for non-technical users is in development.**

## Setting up and running OCI

1. Setting up OpenChess: Insights (OCI) requires python to be installed on the machine. Go to https://www.python.org/downloads/ to download python. Make sure to add it to PATH during installation.

2. Download this respository as a zip file and extract it.

3. Install the packages in requirements.txt

4. Run app.py through an IDE or a CLI. This will start the web app on your local machine at http://127.0.0.1:8000/views/.

5. Go to the url above and input a chess game's PGN. A 30-move game will take about 5 to 10 minutes to process. The output on the IDE or CLI will show some progress bars.

## Notes
The code in this repository is quite cluttered, and contains a lot of bugs.

## To-do
- Make setup easier
- Enable customization of stockfish evaluation for faster analysis
- Fix rating/ELO estimation (formula sometimes overestimates rating)
- Improve layout
- Remove redundant code

## Acknowledgements

JS Chessboard interface from [cm-chessboard](https://github.com/shaack/cm-chessboard)

Chess opening dataset from [lichess-org](https://github.com/lichess-org/chess-openings)

Chess metrics inspired by [mptedesco](https://github.com/mptedesco/python-chess-analysis/tree/master?tab=GPL-3.0-1-ov-file)