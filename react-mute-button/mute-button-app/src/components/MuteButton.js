import OnSvg from '../icons/on'
import OffSvg from '../icons/off'

function MuteButton(props) {
  return (
    <button onClick={ props.toggleMute }>
      { props.isMuted ? <OffSvg /> : <OnSvg />}
    </button>
  )
};

export default MuteButton;