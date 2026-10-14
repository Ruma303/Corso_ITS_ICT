import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faHouse, faUser } from "@fortawesome/free-solid-svg-icons";
import { faGithub } from "@fortawesome/free-brands-svg-icons";
import "./assets/scss/App.scss";

export default function App() {
	return (
		<>
			<FontAwesomeIcon icon={faHouse} />
			<FontAwesomeIcon icon={faUser} size="2x" />
			<FontAwesomeIcon icon={faGithub} />
		</>
	);
}
