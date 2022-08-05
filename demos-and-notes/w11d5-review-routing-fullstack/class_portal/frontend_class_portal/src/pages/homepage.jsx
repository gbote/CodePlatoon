import { Link } from "react-router-dom";

function Homepage() {
    return (
        <div>
            <p>Homepage</p>
            <Link to="grades">Gradebook</Link>
        </div>
    )
}

export default Homepage;