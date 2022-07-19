import { useEffect } from 'react'

function ErrorDisplay(props) {

  useEffect(() => {
    console.log("Error handling...")
  }, [props.message])

  return (
    <div>
    <p className="error">Error: { props.message }</p>
  </div>
)
}

export default ErrorDisplay