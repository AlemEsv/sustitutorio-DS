import igraph as ig
import matplotlib.pyplot as plt
import subprocess

# usar como nodos a los commits que tengo
def crear_DAG():
    # Obtener commits del repositorio actual (últimos 10)
    result = subprocess.run(
        ["git", "log", "--pretty=format:%h|%s|%P", "--all", "-5"],
        capture_output=True,
        text=True,
        cwd="."
    )
    
    commits = []
    parent_map = {}
    
    # Procesar la salida de git log
    for line in result.stdout.strip().split('\n'):
        if line:
            parts = line.split('|')
            commit_hash = parts[0]
            parents = parts[2].split() if len(parts) > 2 and parts[2] else []
            
            commits.append(commit_hash)
            parent_map[commit_hash] = parents
    
    # Crear grafo dirigido
    g = ig.Graph(directed=True)
    
    # Agregar nodos (commits)
    commit_hashes = commits
    g.add_vertices(len(commits))
    g.vs["name"] = commit_hashes
    g.vs["label"] = commit_hashes
    
    # Agregar aristas (relaciones padre-hijo)
    edges = []
    for i, commit_hash in enumerate(commits):
        for parent in parent_map.get(commit_hash, []):
            if parent in commit_hashes:
                parent_idx = commit_hashes.index(parent)
                edges.append((parent_idx, i))  # De padre a hijo
    
    g.add_edges(edges)
    
    ig.summary(g)
    
    fig, ax = plt.subplots(figsize=(12, 30))
    ig.plot(
        g,
        target=ax,
        layout="sugiyama",
        vertex_size=30,
        vertex_color="lightblue",
        edge_color="#222",
        edge_width=1,
        vertex_label_size=8,
    )
    plt.title("Git Commit Graph")
    plt.show()

if __name__ == "__main__":
    crear_DAG()