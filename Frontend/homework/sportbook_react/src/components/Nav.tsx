export interface VoceMenu {
  id: string;
  voce: string;
}

interface NavProps {
  menu: VoceMenu[];
}

export default function Nav({ menu }: NavProps) {
  return (
    <nav className="navbar border-bottom border-secondary-subtle">
      <div className="container justify-content-center">
        <ul className="navbar-nav flex-row gap-4">
          {menu.map(({ id, voce }) => (
            <li className="nav-item" key={id}>
              <a className="nav-link" href={`#${id}`}>
                {voce}
              </a>
            </li>
          ))}
        </ul>
      </div>
    </nav>
  );
}
