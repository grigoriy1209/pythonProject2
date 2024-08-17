import {CarForma} from "../components/CarForma";
import {Cars} from "../components/Cars";
import {Chat} from "../components/Chat";

const CarPage = () => {
    return (
        <div>
            <CarForma/>
            <hr/>
            <Cars/>
            <hr/>
            <Chat/>
        </div>
    );
};

export {CarPage};