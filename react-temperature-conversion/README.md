# React: Temperature Conversion

For this challenge, I convert an existing React project from class-based components to functional components to gain a better understanding about the React Component Lifecycle as well as understanding how to work with the `useEffect()` hook. This will also gave me some more practice with understanding class-based component syntax.

# Initial Set-up

This project utilizes the OpenWeather API. To complete this challenge, I first obtained ny own personal API key through [OpenWeather API](https://home.openweathermap.org/users/sign_up) 

Once I signed up, I was able to find my API key here: [API key](https://home.openweathermap.org/api_keys)

NOTE: This took a few minutes for this key to become active!

Then, I copied my API key value and replace the value of `myOpenWeatherApiKey` at the top of App.jsx with my key value.

Last, I went through the usual set-up commands (`npm install` and `npm run dev`) to get the project running.

# Main Challenge

The main thing I have to work with is the [`useEffect()`](https://reactjs.org/docs/hooks-effect.html) hook to replace the class component life-cycle methods that were implemented previously.

The four components that needed to be refactored are:
- App.jsx
- components/ErrorDisplay.jsx
- components/InputZipCode.jsx
- components/TemperatureDisplay.jsx

IMPORTANT: It was suggested to me that I should strongly consider refactoring the code WITHOUT the api call in place initially. It's possible to accidentally get into an infinite loop when using life-cycle methods / useEffect(), so I added in dummy data and console.log() calls initially to verify the refactor is successful, before using the API call. The OpenWeather API has limits on the number of requests you can make per minute and per day, so if I was to get into an infinite loop with my API call in place, I will likely be banned from using the service temporarily for exceeding the limit!!

Once the refactor is complete, I made sure everything works correctly as it did before!
