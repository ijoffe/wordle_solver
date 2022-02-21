# Wordle Solver v1

## Table of Contents
* [General Information](#general-information)
* [Description](#description)
* [Background](#background)
* [Technologies](#technologies)
* [Instructions](#instructions)
* [Example Usage](#example-usage)

## General Information
This subdirectory contains the first version of code to solve the popular game Wordle. All code was created by me, Isaac Joffe, in February of 2022.

## Description
The aim of this project is to create an algorithm that can successfully find the correct word in the game Wordle within the given number of attempts in all cases. This subdirectory of the repository contains a simple but flawed solution, effective in many cases but unsuccessful and inefficient in others.

One weakness is that the set of possible words are not sorted in any menaingful order, and thus are not selected for guesses with any intentional reason (other than simply being the first to occur alphabetically). This leads to many words that occur in the latter half of the alphabet being more difficult to quickly decipher.

Additionally, there is a small error in the program for dealing with words with repeated letters. When the guessed word has multiple of the same letter and the solution word has that letter ony once, one instance of the letter will be 'black' so all words containing that letter will be incorrectly removed from the set of possible solutions.

## Background
Wordle is a widely popular puzzle game similar to the common board game Mastermind. The game involves using six guesses to try to determine a daily secret word. More information about the game's history and mechanics can be found at the following link: https://en.wikipedia.org/wiki/Wordle. The game can be played at the following link: https://www.nytimes.com/games/wordle/index.html.

When Wordle rapidly became very popluar in late 2021 and early 2022, I struggled compared to my friends and family. After continually getting lower scores, I decided to create an algorithm that could beat most people at the game.

## Technologies
All code contained is written in Python 3.8.10. I created all the code and files in this repository using my personal virtual machine, which runs the Ubuntu distribution of the Linux operating system, through the Sublime Text text editor and the Linux terminal window.

## Instructions
Currently, the program can only be used directly through a terminal window. To run the program, simply enter `python3 wordle_solver.py` in the terminal. Now, begin entering the suggested words into the Wordle website and enter the result that wordle gives ('b' for a black/white letter, 'y' for a yellow letter, and 'g' for a green letter) in the order given into the terminal until the program guesses the correct word.

## Example Usage
```
Try word ouija
Enter Result: bybby
Try word abune
Enter Result: ybgbg
Try word cause
Enter Result: bgggg
Try word hause
Enter Result: bgggg
Try word pause
Enter Result: ggggg
```
