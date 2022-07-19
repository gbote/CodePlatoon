import { Card, Button } from "react-bootstrap";

function Article(props) {
 
  return (
    <Card style={{ width: '100' }}>
      <Card.Title>
          {props.title}<br />
          {props.created_date.substring(0,10)} <br />
          {props.byline && <h5>{props.byline}</h5>}
      </Card.Title>
      {props.image && <Card.Img style={{ width: '400px' }} src={props.image}/>}
      <Card.Body>
        <Card.Text>
          Abstract: <br />{props.abstract}
        </Card.Text>
        <Button variant="primary">Go somewhere</Button>
      </Card.Body>
    </Card>
  )
}

export default Article;