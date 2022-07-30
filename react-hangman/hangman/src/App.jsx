import React, { Component } from 'react';
import './App.css';
import styled from 'styled-components';
import Digits from './components/Digits';
import Title from './components/Title';
import Diagram from './components/Diagram';
import GameOver from './components/GameOver';
import NewGame from './components/NewGame';
import fetchMovies from './components/fetchMovies';

const Name = styled.h1`
  font-size: 56px;
  font-weight: 900;
  font-family: 'Times New Roman', sans-serif;
  margin: 0;
`;

const SubTitle = styled.h3`
  font-size: 22px;
  font-weight: 700;
  font-family: 'Garamond', sans-serif;
  padding: 20px 0;
  text-transform: uppercase;
  margin: 0;
  visibility: ${props => (props.newGame ? 'visible' : 'hidden')};
`;

const Block = styled.div`
  display: flex;
  align-items: flex-start;
  justify-content: center;
  position: relative;
  min-height: 300px;
`;

const letters = /^[a-z0-9]+$/i;
const digits = document.getElementsByClassName('digit');
const winText = `Congratulations! You guessed the movie correctly.`;
const loseText = 'I\'m sorry, but you lost. You guessed the movie incorrectly.';

class App extends Component {
  state = {
    data: [],
    lose: false,
    currentTitle: 0,
    guesses: [],
    currentDiagram: 1,
    goodGuesses: [],
    missedLetters: [],
    newGame: true,
  };
  
  constructor(props) {
    super(props);
    Promise.all([fetchMovies(27), fetchMovies(80), fetchMovies(53), fetchMovies(18), fetchMovies(28), fetchMovies(10751)])
      .then(([horror, crime, thriller, drama, action, family]) => [...horror, ...crime, ...thriller, ...drama, ...action, ...family])
      .then(
        function(titles) {
          const randomTitles = titles.sort(() => {
            return 0.5 - Math.random();
          });
          return this.setState({ data: randomTitles });
        }.bind(this)
      );
  }
  
  getTitle() {
    const currentTitle = this.state.data[this.state.currentTitle].toLowerCase();
    const title = [];
    for (let i = 0; i < currentTitle.length; i++) {
      if (letters.test(currentTitle[i]) || currentTitle[i] === ' ') {
        title.push(currentTitle[i]);
      }
    }
    console.log(`---------> ANSWER: ${currentTitle}`);
    return title.join('');
  }

  handleClick = e => {
    const letter = e.target.textContent.toLowerCase();
    return letter.length > 1 ? null : this.checkLetter(letter);
  };

  handleKeyUp = e => {
    const keyName = e.key;
    if (letters.test(keyName)) {
      return this.isDisabled(keyName) ? null : this.checkLetter(keyName);
    }
  };

  isDisabled(letter) {
    for (let i = 0; i < digits.length; i++) {
      if (digits[i].textContent === letter) {
        return digits[i].hasAttribute('disabled');
      }
    }
  }

  checkLetter = currentLetter => {
    if (this.state.guesses.length > 0) {
      this.state.guesses.map(
        letter =>
          letter === currentLetter
            ? null
            : this.setState({
                guesses: this.state.guesses.concat(currentLetter),
              })
      );
    } else {
      this.setState({
        guesses: this.state.guesses.concat(currentLetter),
      });
    }
    if (!this.getTitle().includes(currentLetter)) {
      this.updateImage();
    } else {
      this.setState(
        {
          goodGuesses: this.state.goodGuesses.concat(currentLetter),
        },
        function() {
          this.isWin();
        }
      );
    }
  };

  updateImage = () => {
    if (this.state.currentDiagram < 6) {
      this.setState({
        currentDiagram: this.state.currentDiagram + 1,
      });
    }
    return this.state.currentDiagram === 6 ? this.gameOver('lose') : null;
  };

  isWin() {
    const lettersList = this.getTitle()
      .replace(/ /g, '')
      .split('')
      .filter((value, index, self) => {
        return self.indexOf(value) === index;
      });
    return lettersList.sort().toString() ===
      this.state.goodGuesses.sort().toString()
      ? this.gameOver('win')
      : null;
  }

  gameOver = result => {
    if (result === 'lose') {
      this.setState({
        lose: true,
        newGame: false,
      });
      this.showRest();
    } else {
      this.setState({
        lose: false,
        newGame: false,
      });
    }
  };

  showRest() {
    const missedLetterList = this.getTitle()
      .split('')
      .filter(letter => !this.state.goodGuesses.includes(letter));
    this.setState({
      missedLetters: missedLetterList.join(''),
    });
  }

  onClickRetry() {
    this.setState({
      currentTitle: this.state.currentTitle + 1,
      guesses: [],
      currentDiagram: 1,
      goodGuesses: [],
      missedLetters: [],
      newGame: true,
    });
  }

  render() {
    return (
      <div className="App" tabIndex="1" onKeyUp={this.handleKeyUp}>
        <Name>Hangman</Name>
        <SubTitle newGame={this.state.newGame}>Guess the movie below!</SubTitle>
        {this.state.data.length > 0 && (
          <div>
            <Block>
              <GameOver
                text={this.state.lose ? loseText : winText}
                newGame={this.state.newGame}
                isLose={this.state.lose}
              />
              <Diagram
                currentDiagram={this.state.currentDiagram}
                newGame={this.state.newGame}
              />
              <NewGame
                onClick={this.onClickRetry.bind(this)}
                newGame={this.state.newGame}
              />
            </Block>

            <Title
              content={this.getTitle()}
              guesses={this.state.guesses}
              missedLetters={this.state.missedLetters}
            />
            <Digits
              guesses={this.state.guesses}
              onClick={this.handleClick}
              newGame={this.state.newGame}
            />
          </div>
        )}
      </div>
    );
  }
}

export default App;