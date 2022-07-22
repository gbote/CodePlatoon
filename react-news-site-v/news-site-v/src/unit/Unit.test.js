import { formatTime } from '../components/Article.jsx';
import axios from 'axios';
// jest.mock('axios') // replaces axios with a mock version


// Make the mock return `true` for the first call,
// and `false` for the second call

describe('the format time function', ()=>{
    describe('when passed valid input ', ()=>{
        it('should return a legible date string', ()=>{
            // can run more code here to test our application
            expect(formatTime(1649168361)).toBe('4/5/2022')

        })
    })

})
