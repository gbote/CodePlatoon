function Selector(props) {
  // render
  const renderChoices = () => {
    return (
      props.data.map((story, index)=> {
        return <option key={index} value={index}>{story.title}</option>
      })
    )
  }

  return (
    <div id="div-selector">
      <span>Select Story: </span>
      <select onChange={(evt)=> props.setSelectedMadLib(props.data[evt.target.value])}>
        { renderChoices() }
      </select>
    </div>
  )
}

export default Selector

// In the selector I am creating a map from the original data. My element is
// story and there will be an index. I will then return an <option> that
// will need to have a key-- which index makes sense. The value will also be
// that as well. The text inside the option will be the story.title which is
// a key in the original data structure.

// After this I need to ensure that when this is selected that it will change 
// the story and the word forms. This will happen with the onChange(). The
// Event from the onChange will take the useState() second variable "setSelectedMadLib"
// and the paretheses will take in the new data that will change the default
// state of the useState(MadLibsData[0]). This will be the data and the 
// event.target.value which is the title which is a key. 

// In addition, this will change the useState() which will change the WordForm
// and Story as well.