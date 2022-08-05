import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from 'axios';

function Gradebook() {
    const [grades, setGrades] = useState([])
    let navigate = useNavigate();

    useEffect(() => {
        axios
            .get('/grades')
            .then((response) => {
                const grades = response.data;
                setGrades(grades.map((grade) => grade.fields))

            })
    }, []);

    console.log(grades)

    const handleClick = (assignmentId) => {
        console.log('handle assignment click, assignment: ', assignmentId);
        navigate(`/assignments/${assignmentId}`)
    }

    return (
        <div>
            <ul>
                {grades.map(({ student, assignment, grade}) => 
                    <li onClick={() => handleClick(assignment)}>
                        Student: {student}, Assignment: {assignment} Grade: {grade}
                    </li>
                )}
            </ul>

        </div>
    )
}

export default Gradebook;