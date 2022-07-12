import "./MyHeader.css"

function MyHeader(props) {
  return (
    <h2 className="my-header">{props.text}</h2>
  );
}

export default MyHeader;