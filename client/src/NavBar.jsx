import { Outlet, Link } from "react-router-dom";

const NavBar = () => {
    return (
        <div className="nav">
            <h3>NLP Land</h3>
            <div>
                <ul>
                    <li>
                    <Link to="/summary">Summarize</Link>
                    </li>
                    <li>
                    <Link to="/sentiment">Sentiment Detection</Link>
                    </li>
                </ul>
            </div>
        </div>
    )
}

export default NavBar;