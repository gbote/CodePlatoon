import './Mole.css'
import MoleIcon from './Mole.svg'

function Mole(props) {

  // calls onMoleWhacked to update points then hides Mole image so it can't be whacked more than once
  const disappearOnClick = (evt) => {
    props.onMoleWhacked()
    const img = evt.currentTarget
    img.style.visibility = "hidden"
  };


  return (
    <div className="den">
      {props.isVisible &&
      <img onClick={ disappearOnClick } src={MoleIcon} className="Mole" alt="Mole" />
      }
    </div>
  );
}

export default Mole;
