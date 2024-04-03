import { Link } from 'react-router-dom';
import styles from './Header.module.css';

const Header = () => {


    return (
        <header className={styles.Header}>
            <Link to="/" className={styles.Logo}>
                <img src="/img/logo.png" alt="Logo" />
            </Link>
        </header>
    );
};

export default Header;
