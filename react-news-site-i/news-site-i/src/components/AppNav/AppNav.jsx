function AppNav(props) {

  return (
    <nav>
      { 
        props.navItems.map((navItem, index)=>{
          return <a href='#' key={index} onClick={ () => props.handleNavClick(navItem.value)}>{navItem.label} | </a>
        })
      }
    </nav>
  )
}

export default AppNav;
