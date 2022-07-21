import {Link} from 'react-router-dom'

function NavBar ({items}){
    // const {items} = props

    const HandleNavBarClick  = (value) => {
        console.log(value)
    }

    
    return(
        <div>
            {items.map((item) => (
                // sending by reference: HandleNavBarClick
                // sending by reference with parameters: () => HandleNavBarClick(item.value)
                <a href="/#/articles/2" key={item.label} onClick={() => HandleNavBarClick(item.value)}> {item.label}</a> 
               
            ))
            }
        </div>
    )
}
export default NavBar;