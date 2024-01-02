# OpenChess: Insights (Beta)

**Updates:**
- Added adjustable stockfish search time and search depth

<hr>

An open-source chess analysis web app runnable in your local machine powered by Stockfish 16 NNUE. Includes:
- move explanations in plain language similar to chess.com's game review
- more metric functionalities than just the eval bar: tension, control, development, and mobility
- accuracy and estimated ELO calculations
- move classifications: excellent, good, inaccuracies, mistakes, blunders, and *brilliant* moves

https://github.com/LinkAnJarad/OpenChess-Insights/assets/79294502/ec2cb92f-52df-4f9b-b121-a2c03639db99


## Setting up and running OCI

1. Setting up OpenChess: Insights (OCI) requires python to be installed on the machine. Go to https://www.python.org/downloads/ to download python. Make sure to add it to PATH during installation.

2. Download this respository as a zip file and extract it.

3. Install the packages in requirements.txt

4. Run the file run.bat to automatically start up the application on your web browser.

5. Go to the url above and input a chess game's PGN. A 30-move game will take about 5 to 10 minutes to process. The output on the IDE or CLI will show some progress bars.

## Notes
The code in this repository is quite cluttered, and contains a lot of bugs.

## To-do
- ARROW KEYS FOR NAVIGATION BETWEEN MOVES
- A PROCESSING PAGE WHEN IT IS ACTUALLY LOADING INSTEAD OF STARING AT SUBMIT
- Make setup easier
- Enable customization of stockfish evaluation for faster analysis
- Fix rating/ELO estimation (formula sometimes overestimates rating)
- Improve layout
- Remove redundant code for speedup

## Acknowledgements

JS Chessboard interface from [cm-chessboard](https://github.com/shaack/cm-chessboard) (MIT License)

Chess opening dataset from [lichess-org](https://github.com/lichess-org/chess-openings)

Chess metrics inspired by [mptedesco](https://github.com/mptedesco/python-chess-analysis/tree/master?tab=GPL-3.0-1-ov-file)

## Like my work?
[Buy me a coffee!](https://www.buymeacoffee.com/linkanjarad)
