import './App.css';
import { BrowserRouter,Routes,Route } from 'react-router-dom';
import Layout from './common/layout/Layout';
import Ocr from './component/ocr/Ocr';
function App() {
  return (
  <>
    <BrowserRouter>
    <Routes>
    <Route path="/" element={<Layout/>}>
    <Route index element={<Ocr/>} />
    </Route>

    
    </Routes>
    </BrowserRouter>
  </>
    );
}

export default App;
