import axios from "axios";
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

function AssignmentPage() {
    const [assignment, setAssignment] = useState(null)
    const { id } = useParams()
    console.log('assignment id param ', id)
    
    useEffect(() => {
        axios
            .get(`/assignments/${id}`)
            .then((response) => {
                const fields = response.data[0].fields;
                console.log('assignment data ', fields);
                setAssignment(fields);
            })
    }, [])

    console.log('assignment state ', assignment);

    return (
        <div>
            {assignment &&
                <div>
                    <h2>Assignment Page</h2>
                    <div>{assignment.description}</div>
                    <a href={assignment.rubric}>Grading Rubric</a>
                    <div>{assignment.title}</div>
                </div>
            }
        </div>
    )
}

export default AssignmentPage;