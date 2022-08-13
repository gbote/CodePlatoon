import { expect, it, describe } from 'vitest'

describe('Math.max', () => {
    describe('with valid inputs', () => {
        it('should return the largest number', () => {
            const biggerNumber = Math.max(1,5)
            expect(biggerNumber).toBe(5)
        })

        it('should handle negative numbers', () => {
            const biggerNumber = Math.max(-20, -3)
            expect(biggerNumber).toBe(-3)
        })

        // This specific example is overkill but is to illustrate the example
        // Example of a test to make sure our output is NOT something
        it('shoud NOT return the smallest number', () => {
            const smallerNumber =  Math.max(1,5)
            expect(smallerNumber).to.not.equal(1)
        })
    })

    describe('with invalid inputs', () => {
        it('cannot return the largest value from strings', () => {
            expect(Math.max('hello', 'b')).toBe(NaN)
        })

    })
})