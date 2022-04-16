import './App.scss';
import {Routes, Route} from "react-router-dom";
import Home from "./components/Home";
import Welcome from "./components/Welcome";

function App() {
  return (
 <>
     <Routes>
       <Route path="/" element={<Welcome />} />
     </Routes>
 </>
  )
}

export default App;
