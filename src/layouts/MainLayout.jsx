import { Outlet, NavLink, ScrollRestoration } from "react-router-dom"
import './MainLayout.css'

const MainLayout = () => {
    return (
      <div className="main-layout">
        <ScrollRestoration />
        <header>
          <nav>
            <h1>LendNU</h1>
            {/* Put profile here */}
          </nav>
        </header>
        <main>
          <Outlet />
        </main>
        <footer>
          <nav>
            <NavLink to="/">Feed</NavLink>
            <NavLink to="publishpage">Post</NavLink>
          </nav>
        </footer>
      </div>
    )
  }

  export default MainLayout;