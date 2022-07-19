function AppNav(props) {

  return (
    <nav className="section">
      {props.navItems.map((item) => (
      <a className="link nav__link" key={item.label} href="" onClick={props.handleNavClick(item.value)}>
        {item.label}
      </a>
      ))}
    </nav>
  )
}

export default AppNav;


// // class-based component equivalent code:
// import React, { Component } from 'react';

// class AppNav extends Component {
  
//   render() {
//     return (
//       <nav>
//       {
//         this.props.navItems.map((navItem) =>
//           <a href="#" onClick={ () => this.props.handleNavClick(navItem.value)} >
//             { navItem.label } |
//           </a>
//         )
//       }
//       </nav>
//     )
//   }
// }