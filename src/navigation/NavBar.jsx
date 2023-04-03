import { Outlet, NavLink, ScrollRestoration } from "react-router-dom"
import './NavBar.css'

const NavBar = () => {
    return (
      <div className="main-layout">
        <header>
          <nav>
            <h1 className="mx-auto">LendNU</h1>
            {/* Put profile here */}
            {/* Put login here */}
          </nav>
        </header>
        <main>
          <Outlet />
        </main>
        <footer>
          <nav >
            <NavLink to="/">Feed</NavLink>
            <NavLink to="publishpage">Post</NavLink>
            {/* Put profile here */}
            {/* Put login here */}
          </nav>
        </footer>
      </div>
    );
  }

  export default NavBar;