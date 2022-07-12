import UsaStateData from "../statedata/index.js"

function StateDropDown(props) {
  // render
  const populateStateDropDown = () => {
    let elements = [];
    for (let i = 0; i < UsaStateData.length; i++) {
      elements.push(
        <option key={`state-${i}`} 
          value={ UsaStateData[i]["alpha-2"] }>
              { UsaStateData[i]["name"] }
        </option>
        );
    }
    // return JSX
    return elements; // this array gets converted to individual JSX elements
  }

  return (
    <div>
      <select onChange={ 
        (evt) => props.setStateAbbr(evt.currentTarget.value)
      }>
        { populateStateDropDown() }
      </select>
    </div>
  );
};


export default StateDropDown;