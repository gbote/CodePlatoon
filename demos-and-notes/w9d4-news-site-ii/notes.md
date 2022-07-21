# News Site II

## Topics:
- use client side routing / react router
- Use Bootstrap components


```sh
npm install react-router-dom --save
```

```js
import { HashRouter as Router, Routes, Route } from 'react-router-dom';
```

## 2 types of routing with react-router:
- Hash router: if a URl # then it will not route server-side. It will only route on the client's side. And no data will be sent to the server. 

- Browser router: doesn't use #. it uses extra js to avoid sending the new URL to the server.