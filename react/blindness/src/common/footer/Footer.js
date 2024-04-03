import React from 'react';
import styles from './Footer.module.css';
const Footer = () => {
    return (
        <footer className={styles.foot}>
        <p>© 2024 Blindness. All rights reserved.
            <br/>
            시각 장애인을 위한 웹 프로젝트
        </p>
    </footer>
    );
};

export default Footer;